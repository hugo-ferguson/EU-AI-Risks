import { sampleReport } from "../data/sampleReport";

const API_URL = import.meta.env.VITE_API_URL;

export async function assessRequirementDocument(file) {
  if (!file) {
    throw new Error("Please upload a requirements document first.");
  }

  if (!API_URL) {
    throw new Error(
      "Backend API is not connected. Add VITE_API_URL=http://localhost:8000 to frontend/.env, then restart npm run dev."
    );
  }

  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_URL}/api/assess-risks`, {
    method: "POST",
    body: formData
  });

  if (!response.ok) {
    let message = `Risk assessment failed: ${response.status}`;
    try {
      const errorBody = await response.json();
      if (errorBody?.detail) message = errorBody.detail;
    } catch {
      // Keep the fallback message if the server did not return JSON.
    }
    throw new Error(message);
  }

  return response.json();
}

export function loadDemoReport() {
  return sampleReport;
}
