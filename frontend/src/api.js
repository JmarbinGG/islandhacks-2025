import axios from "axios";

const API_BASE = process.env.REACT_APP_API_URL || "http://localhost:5000";

export const api = {
  ping: async () => {
    const res = await axios.get(`${API_BASE}/api/ping`);
    return res.data;
  },

  analyzeData: async (data) => {
    const res = await axios.post(`${API_BASE}/api/analyze`, data);
    return res.data;
  },

  analyzeFile: async (file) => {
    const form = new FormData();
    form.append("file", file);
    const res = await axios.post(`${API_BASE}/api/analyze`, form, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    return res.data;
  },
};