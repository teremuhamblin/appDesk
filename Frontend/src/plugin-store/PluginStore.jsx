import PluginList from "./components/PluginList";
import PluginInstaller from "./components/PluginInstaller";

export default function PluginStore() {
  return (
    <div style={{ padding: 20 }}>
      <h1>Plugin Store</h1>

      <PluginInstaller />
      <PluginList />
    </div>
  );
}
