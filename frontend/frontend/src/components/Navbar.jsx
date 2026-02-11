import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="flex justify-between items-center px-8 py-4 bg-slate-900 shadow-md ">
      <h1 className="text-xl font-bold text-indigo-400">
        Lost & Found AI
      </h1>
      <div className="space-x-6">
        <Link to="/" className="hover:text-indigo-400">Search</Link>
        <Link to="/add" className="hover:text-indigo-400">Add Found Item</Link>
      </div>
    </nav>
  );
}
