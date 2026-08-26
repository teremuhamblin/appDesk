import axios from "axios";
import { useEffect, useState } from "react";

export default function PluginList() {
  const [plugins, setPlugins] = useState([]);

  useEffect(() => {
    axios.get("/api/plugins/list/").then(res => setPlugins(res.data));
  }, []);

  return (
    <div>
      <h2>Plugins installés</h2>
      <ul>
        {plugins.map(p => (
          <li key={p.name}>
            {p.name} — v{p.version}
          </li>
        ))}
      </ul>
    </div>
  );
}
