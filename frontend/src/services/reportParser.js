export function parseMarkdownReport(markdown) {
  const summary = { high: 0, medium: 0, low: 0 };
  ["High", "Medium", "Low"].forEach((level) => {
    const match = markdown.match(new RegExp(`-\\s*${level}:\\s*(\\d+)`, "i"));
    if (match) summary[level.toLowerCase()] = Number(match[1]);
  });

  const sections = markdown.split(/\n---\n/g);
  const findings = sections
    .map((section) => {
      const id = section.match(/###\s+(\S+)/)?.[1];
      if (!id) return null;

      const level = section.match(/\*\*Risk level:\*\*\s*(\w+)/i)?.[1]?.toLowerCase() || "low";
      const requirement = section.match(/\*\*Requirement:\*\*\s*([\s\S]*?)(?=\n\n\*\*Analysis:\*\*|\n\n|$)/i)?.[1]?.trim() || "";
      const analysis = section.match(/\*\*Analysis:\*\*\s*([\s\S]*?)(?=\n\n\*\*Risks:\*\*|\n\n---|$)/i)?.[1]?.trim().replace(/\\n/g, " ") || "";

      const risksBlock = section.match(/\*\*Risks:\*\*\s*([\s\S]*?)(?=\n\n\*\*Cited provisions:\*\*|\n\n---|$)/i)?.[1] || "";
      const lines = risksBlock.split("\n").map((line) => line.trim());
      const risks = [];

      lines.forEach((line, index) => {
        if (!line.startsWith("- ")) return;
        const categoryLine = lines[index + 1] || "";
        const actionLine = lines[index + 2] || "";
        risks.push({
          description: line.slice(2),
          category: categoryLine.includes("Category:")
            ? categoryLine.split("Category:")[1].trim().replaceAll("`", "")
            : "general",
          action: actionLine.includes("Suggested engineering action:")
            ? actionLine.split("Suggested engineering action:")[1].trim()
            : "Review this requirement manually."
        });
      });

      const recommendationsBlock = section.match(/\*\*Recommendations:\*\*\s*([\s\S]*?)(?=\n\n---|$)/i)?.[1] || "";
      const recommendations = recommendationsBlock
        .split("\n")
        .map((line) => line.trim())
        .filter((line) => line.startsWith("- "))
        .map((line) => line.slice(2));

      return { id, level, requirement, analysis, risks, recommendations };
    })
    .filter(Boolean);

  return { summary, findings };
}
