function RootCauseCard({ causes }) {

  if (!causes) return null;

  return (
    <div className="card">

      <h2>🔥 Root Causes</h2>

      <ul>
        {causes.map((cause, index) => (
          <li key={index}>{cause}</li>
        ))}
      </ul>

    </div>
  );
}

export default RootCauseCard;