import axios from "axios";
import { useEffect, useState } from "react";

export default function App() {
  const [plugins, setPlugins] = useState([]);
  const [url, setUrl] = useState("");

  useEffect(() => {
    axios.get("/api/plugins/list/").then(res => setPlugins(res.data));
  }, []);

  const installPlugin = () => {
    axios.post("/api/plugins/install/", { url }).then(() => {
      alert("Plugin installé");
    });
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Plugin Store</h1>

      <h2>Plugins installés</h2>
      <ul>
        {plugins.map(p => (
          <li key={p.name}>
            {p.name} — v{p.version}
          </li>
        ))}
      </ul>

      <h2>Installer un plugin</h2>
      <input
        placeholder="URL du ZIP"
        value={url}
        onChange={e => setUrl(e.target.value)}
      />
      <button onClick={installPlugin}>Installer</button>
    </div>
  );
}
