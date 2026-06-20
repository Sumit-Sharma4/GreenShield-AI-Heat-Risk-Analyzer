import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  ResponsiveContainer
} from "recharts";

function LandcoverChart({ landcover }) {

  const data = [
    {
      name: "Tree",
      value: landcover.tree_cover
    },
    {
      name: "Built-up",
      value: landcover.built_up
    },
    {
      name: "Water",
      value: landcover.water
    },
    {
      name: "Grass",
      value: landcover.grass
    },
    {
      name: "Cropland",
      value: landcover.cropland
    },
    {
      name: "Shrub",
      value: landcover.shrub
    }
  ];

  const COLORS = [
    "#2e7d32",
    "#d32f2f",
    "#1976d2",
    "#66bb6a",
    "#f9a825",
    "#8d6e63"
  ];

  return (
    <div style={{ width: "100%", height: 350 }}>

      <h3>📊 Landcover Distribution</h3>

      <ResponsiveContainer>

        <PieChart>

          <Pie
           data={data}
           dataKey="value"
           nameKey="name"
           outerRadius={120}
           >

            {data.map((entry, index) => (
              <Cell
                key={index}
                fill={COLORS[index]}
              />
            ))}

          </Pie>

          <Tooltip />
          <Legend />

        </PieChart>

      </ResponsiveContainer>

    </div>
  );
}

export default LandcoverChart;