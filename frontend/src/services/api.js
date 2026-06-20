import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000"
});

export const exportHotspotsCSV = (city) => {
  window.open(
    `http://127.0.0.1:8000/export/hotspots/${city}`
  );
};

export const analyzeCity = async (city) => {
  const response = await API.get(`/analyze/${city}`);
  return response.data;
};

export const getHotspots = async (city) => {
  const response = await API.get(`/hotspots/${city}`);
  return response.data;
};

export const getDashboard = async (city) => {
  const response = await API.get(`/dashboard/${city}`);
  return response.data;
};