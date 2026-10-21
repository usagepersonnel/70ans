"""Extract text from an Excalidraw file and export to Markdown."""

import argparse
import json
from pathlib import Path

ZERO_WIDTH_CHARS = "\u200b\u200c\u200d\ufeff"


def clean_text(text: str) -> str:
    """Strip zero-width characters and surrounding whitespace."""
    return text.translate(str.maketrans("", "", ZERO_WIDTH_CHARS)).strip()


def extract_text_elements(data: dict) -> list[dict]:
    """Return all non-deleted text elements with meaningful content."""
    elements = data.get("elements", [])
    result = []
    seen: set[str] = set()
    for el in elements:
        if el.get("type") != "text":
            continue
        if el.get("isDeleted", False):
            continue
        text = clean_text(el.get("text", ""))
        if not text:
            continue
        if text in seen:
            continue
        seen.add(text)
        el = dict(el)
        el["_clean_text"] = text
        result.append(el)
    return result


def build_font_size_map(elements: list[dict]) -> dict[float | None, int]:
    """Map font sizes to Markdown heading levels (1-3) or 0 for body text.

    The largest distinct font sizes get heading levels; the rest are body.
    """
    sizes = sorted(
        {el.get("fontSize") or 0 for el in elements if el.get("fontSize")},
        reverse=True,
    )
    size_map: dict[float | None, int] = {}
    for i, size in enumerate(sizes):
        if i < 3:
            size_map[size] = i + 1  # h1, h2, h3
        else:
            size_map[size] = 0  # body
    size_map[None] = 0
    return size_map


def group_by_frame(
    text_elements: list[dict], frame_elements: list[dict],
) -> tuple[list[dict], list[tuple[dict, list[dict]]]]:
    """Split text elements into unframed and framed groups.

    Returns (unframed_list, [(frame_element, [text_elements]), ...]).
    Frame groups are sorted spatially by the frame's position.
    """
    unframed = []
    framed: dict[str, list[dict]] = {}

    for el in text_elements:
        frame_id = el.get("frameId")
        if frame_id is None:
            unframed.append(el)
        else:
            framed.setdefault(frame_id, []).append(el)

    frame_by_id = {f["id"]: f for f in frame_elements}
    framed_sorted = []
    for frame_id, elements in framed.items():
        frame_el = frame_by_id.get(frame_id, {"id": frame_id, "y": 0, "x": 0})
        framed_sorted.append((frame_el, elements))
    framed_sorted.sort(key=lambda pair: (pair[0].get("y", 0), pair[0].get("x", 0)))

    return unframed, framed_sorted


def sort_spatially(elements: list[dict]) -> list[dict]:
    """Sort elements by y (top-to-bottom), then x (left-to-right)."""
    return sorted(elements, key=lambda el: (el.get("y", 0), el.get("x", 0)))


def cluster_spatially(elements: list[dict], threshold: float = 50.0) -> list[list[dict]]:
    """Group elements into clusters based on vertical proximity.

    Elements within `threshold` pixels vertically of the previous element
    in the sorted order belong to the same cluster.
    """
    if not elements:
        return []
    sorted_els = sort_spatially(elements)
    clusters = [[sorted_els[0]]]
    for el in sorted_els[1:]:
        prev = clusters[-1][-1]
        if abs(el.get("y", 0) - prev.get("y", 0)) <= threshold:
            clusters[-1].append(el)
        else:
            clusters.append([el])
    return clusters


def format_heading(text: str, level: int) -> str:
    """Format text as a Markdown heading at the given level."""
    return f"{'#' * level} {text}"


def build_markdown(
    unframed: list[dict],
    framed: list[tuple[dict, list[dict]]],
    size_map: dict[float | None, int],
) -> str:
    """Build the Markdown string from grouped text elements."""
    blocks: list[str] = []

    if unframed:
        clusters = cluster_spatially(unframed)
        for i, cluster in enumerate(clusters):
            if i > 0:
                blocks.append("---")
            for el in sort_spatially(cluster):
                text = el["_clean_text"]
                level = size_map.get(el.get("fontSize"), 0)
                blocks.append(format_heading(text, level) if level else text)

    for frame_el, elements in framed:
        if blocks:
            blocks.append("---")
        sorted_els = sort_spatially(elements)
        title_el = max(sorted_els, key=lambda el: el.get("fontSize") or 0)
        title_level = size_map.get(title_el.get("fontSize"), 2)
        title_level = min(title_level, 2) if title_level else 2
        blocks.append(format_heading(title_el["_clean_text"], title_level))
        for el in sorted_els:
            if el is title_el:
                continue
            text = el["_clean_text"]
            level = size_map.get(el.get("fontSize"), 0)
            blocks.append(format_heading(text, level) if level else text)

    return "\n\n".join(blocks) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract text from an Excalidraw file and export to Markdown."
    )
    parser.add_argument(
        "input",
        help="Input .excalidraw filename (relative to input/ folder)",
    )
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Output .md filename (relative to output/ folder). Defaults to input stem + .md",
    )
    args = parser.parse_args()

    base = Path(__file__).parent
    input_path = base / "input" / args.input

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if args.output:
        output_name = args.output
    else:
        output_name = Path(args.input).stem + ".md"
    output_path = base / "output" / output_name
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    text_elements = extract_text_elements(data)
    frame_elements = [
        el for el in data.get("elements", [])
        if el.get("type") == "frame" and not el.get("isDeleted", False)
    ]
    size_map = build_font_size_map(text_elements)
    unframed, framed = group_by_frame(text_elements, frame_elements)
    markdown = build_markdown(unframed, framed, size_map)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"Extracted {len(text_elements)} text elements -> {output_path}")


if __name__ == "__main__":
    main()
