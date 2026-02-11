export default function ItemCard({ item }) {
  return (
    <div className="bg-slate-900 rounded-xl overflow-hidden shadow-lg hover:scale-105 transition">
      <img
        src={item.image_url}
        className="h-48 w-full object-cover"
      />
      <div className="p-4">
        <p className="text-sm text-gray-400">
          Similarity: {(item.similarity * 100).toFixed(2)}%
        </p>
        <p className="mt-1">{item.description}</p>
      </div>
    </div>
  );
}
