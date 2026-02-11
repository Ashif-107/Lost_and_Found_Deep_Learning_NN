import { useLocation } from "react-router-dom";
import ItemCard from "../components/ItemCard";

export default function Results() {
  const { state } = useLocation();

  return (
    <div className="p-10">
      <h2 className="text-2xl mb-6">Matching Items</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {state?.map((item, i) => (
          <ItemCard key={i} item={item} />
        ))}
      </div>
    </div>
  );
}
