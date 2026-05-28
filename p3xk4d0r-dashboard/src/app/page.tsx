"use client";

import { useState } from "react";

export default function Home() {

  const [topic, setTopic] = useState("");

  const [useMemory, setUseMemory] = useState(true);

  const [useGeo, setUseGeo] = useState(true);
  const [useTech, setUseTech] = useState(true);
  const [useRisk, setUseRisk] = useState(true);

  const [loading, setLoading] = useState(false);

  const [result, setResult] = useState<any>(null);

  async function generateReport() {

    setLoading(true);

    try {

      const response = await fetch(
        "https://p3xk4d0r.onrender.com/generate-report",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json"
          },

          body: JSON.stringify({
            topic: topic,

            use_memory: useMemory,

            use_geopolitical: useGeo,
            use_technical: useTech,
            use_risk: useRisk
          })
        }
      );

      const data = await response.json();

      setResult(data);

    } catch (error) {

      console.error(error);

    }

    setLoading(false);
  }

  return (

    <main className="p-10 max-w-4xl mx-auto">

      <h1 className="text-4xl font-bold mb-8">
        P3XK4D0R Dashboard
      </h1>

      <textarea
        className="w-full border p-4 rounded mb-6"
        rows={4}
        placeholder="Enter analysis topic..."
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />

      <div className="space-y-2 mb-6">

        <label className="block">
          <input
            type="checkbox"
            checked={useMemory}
            onChange={() => setUseMemory(!useMemory)}
          />
          {" "}Use Semantic Memory
        </label>

        <label className="block">
          <input
            type="checkbox"
            checked={useGeo}
            onChange={() => setUseGeo(!useGeo)}
          />
          {" "}Geopolitical Agent
        </label>

        <label className="block">
          <input
            type="checkbox"
            checked={useTech}
            onChange={() => setUseTech(!useTech)}
          />
          {" "}Technical Agent
        </label>

        <label className="block">
          <input
            type="checkbox"
            checked={useRisk}
            onChange={() => setUseRisk(!useRisk)}
          />
          {" "}Risk Agent
        </label>

      </div>

      <button
        onClick={generateReport}
        disabled={loading}
        className="bg-black text-white px-6 py-3 rounded"
      >
        {loading ? "Generating..." : "Generate Report"}
      </button>

      {result && (

        <div className="mt-10 border p-4 rounded">

          <h2 className="text-2xl font-bold mb-4">
            Report Result
          </h2>

          <pre className="overflow-auto text-sm">
            {JSON.stringify(result, null, 2)}
          </pre>

        </div>
      )}

    </main>
  );
}