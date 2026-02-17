'use client';

import { useState } from 'react';

const FLASK_API_URL = process.env.NEXT_PUBLIC_FLASK_API_URL || 'http://localhost:5328';

interface ApiResponse {
  status?: string;
  message?: string;
  method?: string;
  received_data?: Record<string, unknown>;
  total?: number;
  average?: number;
  count?: number;
}

export default function ApiTest() {
  const [response, setResponse] = useState<ApiResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const testGet = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(`${FLASK_API_URL}/api/test`);
      const data = await res.json();
      setResponse(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to connect to Flask API');
    } finally {
      setLoading(false);
    }
  };

  const testPost = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(`${FLASK_API_URL}/api/test`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: 'Test User', action: 'testing' }),
      });
      const data = await res.json();
      setResponse(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to connect to Flask API');
    } finally {
      setLoading(false);
    }
  };

  const testCalculate = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(`${FLASK_API_URL}/api/calculate-points`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ points: [10, 20, 30, 40, 50] }),
      });
      const data = await res.json();
      setResponse(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to connect to Flask API');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-8 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">Flask API Integration Test</h1>
      
      <div className="flex gap-4 mb-6">
        <button
          onClick={testGet}
          disabled={loading}
          className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50"
        >
          Test GET
        </button>
        <button
          onClick={testPost}
          disabled={loading}
          className="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700 disabled:opacity-50"
        >
          Test POST
        </button>
        <button
          onClick={testCalculate}
          disabled={loading}
          className="px-4 py-2 bg-purple-600 text-white rounded hover:bg-purple-700 disabled:opacity-50"
        >
          Test Calculate
        </button>
      </div>

      {error && (
        <div className="p-4 mb-4 bg-red-100 border border-red-400 text-red-700 rounded">
          {error}
        </div>
      )}

      {response && (
        <div className="p-4 bg-gray-100 rounded">
          <h2 className="font-semibold mb-2">Response:</h2>
          <pre className="whitespace-pre-wrap">{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
