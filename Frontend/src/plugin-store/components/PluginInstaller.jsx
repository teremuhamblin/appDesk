import axios from "axios";
import { useState } from "react";

export default function PluginInstaller() {
  const [url, setUrl] = useState("");

  const installPlugin = () => {
    axios.post("/api/plugins/install/", { url }).then(() => {
      alert("Plugin installé");
    });
  };

  return (
    <div>
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
