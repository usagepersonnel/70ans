"""Extract text from an Excalidraw file and export to Markdown."""

import argparse
import json
from pathlib import Path


def extract_text_elements(data: dict) -> list[dict]:
    """Return all non-deleted text elements from the parsed Excalidraw JSON."""
    elements = data.get("elements", [])
    return [
        el for el in elements
        if el.get("type") == "text"
        and not el.get("isDeleted", False)
        and el.get("text", "").strip()
    ]


def group_by_frame(text_elements: list[dict]) -> tuple[list[dict], dict[str, list[dict]]]:
    """Split text elements into unframed and framed groups.

    Returns (unframed_list, {frame_id: [elements]}).
    """
    unframed = []
    framed: dict[str, list[dict]] = {}

    for el in text_elements:
        frame_id = el.get("frameId")
        if frame_id is None:
            unframed.append(el)
        else:
            framed.setdefault(frame_id, []).append(el)

    return unframed, framed


def sort_spatially(elements: list[dict]) -> list[dict]:
    """Sort elements by y (top-to-bottom), then x (left-to-right)."""
    return sorted(elements, key=lambda el: (el.get("y", 0), el.get("x", 0)))


def build_markdown(unframed: list[dict], framed: dict[str, list[dict]]) -> str:
    """Build the Markdown string from grouped text elements."""
    sections: list[str] = []

    if unframed:
        for el in sort_spatially(unframed):
            sections.append(el["text"].strip())

    for frame_id, elements in framed.items():
        if sections:
            sections.append("\n---\n")
        for el in sort_spatially(elements):
            sections.append(el["text"].strip())

    return "\n\n".join(sections) + "\n"


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
    unframed, framed = group_by_frame(text_elements)
    markdown = build_markdown(unframed, framed)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"Extracted {len(text_elements)} text elements -> {output_path}")


if __name__ == "__main__":
    main()
