import React from "react";
import PluginStore from "./plugin-store";

function App() {
  return (
    <div style={{ fontFamily: "Arial", padding: "20px" }}>
      <h1>appDesk Frontend</h1>

      {/* Module Plugin Store */}
      <PluginStore />
    </div>
  );
}

export default App;
