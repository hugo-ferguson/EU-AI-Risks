import { useMemo, useState } from "react";
import {
  AlertTriangle,
  BarChart3,
  CheckCircle2,
  ClipboardCheck,
  FileText,
  Filter,
  Layers3,
  Loader2,
  Search,
  ShieldCheck,
  Upload
} from "lucide-react";
import { sampleReport } from "./data/sampleReport";
import { assessRequirementDocument, loadDemoReport } from "./services/riskApi";

const LEVELS = ["all", "high", "medium", "low"];
const REQUIREMENT_FILE_TYPES = ".json,.txt,.md,.markdown,.pdf,.docx";

function countFindings(report) {
  const counts = { high: 0, medium: 0, low: 0 };
  report.findings.forEach((finding) => {
    counts[finding.level] = (counts[finding.level] || 0) + 1;
  });
  return counts;
}

function prettyCategory(category = "") {
  return category.replaceAll("_", " ").replaceAll("-", " ");
}

function getCategories(report) {
  const categories = new Set();
  report.findings.forEach((finding) => {
    finding.risks?.forEach((risk) => {
      if (risk.category) categories.add(risk.category);
    });
  });
  return ["all", ...Array.from(categories).sort()];
}

function StatCard({ title, value, helper, icon: Icon }) {
  return (
    <div className="stat-card">
      <div className="stat-icon"><Icon size={18} /></div>
      <div>
        <p>{title}</p>
        <strong>{value}</strong>
        <span>{helper}</span>
      </div>
    </div>
  );
}

function RiskPill({ level }) {
  return <span className={`risk-pill ${level}`}>{level}</span>;
}

function PipelineStep({ number, title, text }) {
  return (
    <div className="pipeline-step">
      <span>{number}</span>
      <div>
        <strong>{title}</strong>
        <p>{text}</p>
      </div>
    </div>
  );
}

function FindingCard({ finding, active, onClick }) {
  const categories = [...new Set((finding.risks || []).map((risk) => risk.category).filter(Boolean))];

  return (
    <button className={`finding-card ${active ? "active" : ""}`} onClick={onClick}>
      <div className="finding-topline">
        <strong>{finding.id}</strong>
        <RiskPill level={finding.level} />
      </div>
      <p>{finding.requirement}</p>
      <div className="category-row">
        {categories.slice(0, 3).map((category) => (
          <span key={category}>{prettyCategory(category)}</span>
        ))}
      </div>
    </button>
  );
}

function FindingDetail({ finding }) {
  if (!finding) {
    return (
      <div className="empty-state">
        <ShieldCheck size={36} />
        <h3>Select a finding</h3>
        <p>Choose a requirement from the left to review its risk mapping and suggested engineering actions.</p>
      </div>
    );
  }

  return (
    <div className="detail-panel">
      <div className="detail-header">
        <div>
          <span className="eyebrow">Requirement finding</span>
          <h2>{finding.id}</h2>
        </div>
        <RiskPill level={finding.level} />
      </div>

      <section>
        <h3>Requirement</h3>
        <p className="requirement-text">{finding.requirement}</p>
      </section>

      <section>
        <h3>Risk analysis</h3>
        <p>{finding.analysis}</p>
      </section>

      <section>
        <h3>Mapped obligations</h3>
        <div className="risk-list">
          {(finding.risks || []).length === 0 ? (
            <div className="positive-card">
              <CheckCircle2 size={18} />
              <p>No retained requirement-level risk. This requirement appears to act as a safeguard/control.</p>
            </div>
          ) : (
            finding.risks.map((risk, index) => (
              <div className="risk-item" key={`${risk.description}-${index}`}>
                <div>
                  <span>{prettyCategory(risk.category)}</span>
                  <p>{risk.description}</p>
                </div>
                <small>{risk.action}</small>
              </div>
            ))
          )}
        </div>
      </section>

      <section>
        <h3>Recommended next steps</h3>
        <ul className="recommendations">
          {(finding.recommendations || []).length > 0 ? (
            finding.recommendations.map((recommendation, index) => <li key={index}>{recommendation}</li>)
          ) : (
            <li>Confirm the mapping with a human reviewer before using it for compliance decisions.</li>
          )}
        </ul>
      </section>
    </div>
  );
}

export default function App() {
  const [report, setReport] = useState(sampleReport);
  const [selectedId, setSelectedId] = useState(sampleReport.findings[0]?.id);
  const [levelFilter, setLevelFilter] = useState("all");
  const [categoryFilter, setCategoryFilter] = useState("all");
  const [query, setQuery] = useState("");
  const [requirementsFile, setRequirementsFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("Demo report loaded");

  const counts = useMemo(() => countFindings(report), [report]);
  const categories = useMemo(() => getCategories(report), [report]);

  const filteredFindings = useMemo(() => {
    return report.findings.filter((finding) => {
      const matchesLevel = levelFilter === "all" || finding.level === levelFilter;
      const riskCategories = (finding.risks || []).map((risk) => risk.category);
      const matchesCategory = categoryFilter === "all" || riskCategories.includes(categoryFilter);
      const haystack = `${finding.id} ${finding.requirement} ${finding.analysis}`.toLowerCase();
      const matchesQuery = haystack.includes(query.toLowerCase());
      return matchesLevel && matchesCategory && matchesQuery;
    });
  }, [report, levelFilter, categoryFilter, query]);

  const selectedFinding = useMemo(() => {
    return report.findings.find((finding) => finding.id === selectedId) || filteredFindings[0];
  }, [report, selectedId, filteredFindings]);

  async function runAssessment() {
    setLoading(true);
    setStatus("Running assessment from uploaded requirements document...");
    try {
      const nextReport = await assessRequirementDocument(requirementsFile);
      setReport(nextReport);
      setSelectedId(nextReport.findings[0]?.id);
      setStatus(`Assessment complete: ${nextReport.findings.length} requirements reviewed`);
    } catch (error) {
      setStatus(error.message || "Could not run assessment");
    } finally {
      setLoading(false);
    }
  }

  function handleRequirementsUpload(event) {
    const file = event.target.files?.[0];
    if (!file) return;
    setRequirementsFile(file);
    setStatus(`Ready to assess ${file.name}`);
  }

  function useDemoReport() {
    const demo = loadDemoReport();
    setReport(demo);
    setSelectedId(demo.findings[0]?.id);
    setStatus("Demo report loaded");
  }

  return (
    <main className="app-shell">
      <nav className="top-nav">
        <div className="brand">
          <div className="brand-mark"><ClipboardCheck size={21} strokeWidth={2.35} /></div>
          <div>
            <strong>EU AI Risk Mapper</strong>
            <span>Proof of concept</span>
          </div>
        </div>
        <div className="nav-status">
          <span className="status-dot" />
          {status}
        </div>
      </nav>

      <section className="hero">
        <div>
          <span className="eyebrow">Traceable requirements review</span>
          <h1>Map software requirements to EU AI Act risk obligations.</h1>
          <p>
            Upload a requirements document, run the KG + LLM risk assessment pipeline, and review mapped
            obligation categories, remaining gaps, existing safeguards, and practical engineering actions.
          </p>
          <div className="hero-actions">
            <button className="primary-btn" onClick={runAssessment} disabled={loading || !requirementsFile}>
              {loading ? <Loader2 className="spin" size={16} /> : <BarChart3 size={16} />}
              Run assessment
            </button>
            <button className="secondary-btn" type="button" onClick={useDemoReport}>Load demo</button>
          </div>
        </div>

        <div className="pipeline-card">
          <PipelineStep number="01" title="Upload" text="Upload JSON, TXT, MD, PDF, or DOCX requirements." />
          <PipelineStep number="02" title="Assess" text="Run semantic-profile EU AI Act mapping." />
          <PipelineStep number="03" title="Review" text="Surface risks, controls, and engineering actions." />
        </div>
      </section>

      <section className="workspace-grid">
        <aside className="input-panel">
          <div className="panel-heading">
            <FileText size={18} />
            <div>
              <strong>Requirements document</strong>
              <span>Upload JSON, TXT, MD, PDF, or DOCX</span>
            </div>
          </div>

          <label className={`upload-dropzone ${requirementsFile ? "has-file" : ""}`}>
            <Upload size={28} />
            <strong>{requirementsFile ? requirementsFile.name : "Upload requirements document"}</strong>
            <span>
              {requirementsFile
                ? "Ready to run assessment"
                : "Use your requirements JSON or an SRS-style document with shall/should/must statements."}
            </span>
            <input type="file" accept={REQUIREMENT_FILE_TYPES} onChange={handleRequirementsUpload} />
          </label>

          <button className="full-width-btn" onClick={runAssessment} disabled={loading || !requirementsFile}>
            {loading ? <Loader2 className="spin" size={16} /> : <BarChart3 size={16} />}
            {loading ? "Running..." : "Run assessment"}
          </button>

          <div className="input-note">
            <strong>Current flow</strong>
            <p>
              The frontend sends the uploaded requirements document to the Python API, which extracts requirements,
              runs the existing risk assessment pipeline, and returns the report to this dashboard.
            </p>
          </div>
        </aside>

        <section className="results-panel">
          <div className="stats-grid">
            <StatCard title="Total findings" value={report.findings.length} helper="requirements reviewed" icon={Layers3} />
            <StatCard title="High" value={counts.high} helper="critical gaps" icon={AlertTriangle} />
            <StatCard title="Medium" value={counts.medium} helper="needs review" icon={BarChart3} />
            <StatCard title="Low" value={counts.low} helper="controls or clarification" icon={ShieldCheck} />
          </div>

          <div className="filters">
            <div className="search-box">
              <Search size={16} />
              <input placeholder="Search requirements..." value={query} onChange={(event) => setQuery(event.target.value)} />
            </div>
            <div className="filter-group">
              <Filter size={15} />
              <select value={levelFilter} onChange={(event) => setLevelFilter(event.target.value)}>
                {LEVELS.map((level) => <option key={level} value={level}>{level}</option>)}
              </select>
              <select value={categoryFilter} onChange={(event) => setCategoryFilter(event.target.value)}>
                {categories.map((category) => <option key={category} value={category}>{prettyCategory(category)}</option>)}
              </select>
            </div>
          </div>

          <div className="review-layout">
            <div className="findings-list">
              {filteredFindings.map((finding) => (
                <FindingCard
                  key={finding.id}
                  finding={finding}
                  active={selectedFinding?.id === finding.id}
                  onClick={() => setSelectedId(finding.id)}
                />
              ))}
              {filteredFindings.length === 0 && <p className="no-results">No findings match the current filters.</p>}
            </div>
            <FindingDetail finding={selectedFinding} />
          </div>
        </section>
      </section>
    </main>
  );
}
