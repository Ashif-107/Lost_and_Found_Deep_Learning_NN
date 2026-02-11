export default function ImageUpload({ onUpload }) {
  return (
    <label className="cursor-pointer border-2 border-dashed border-indigo-400 p-8 rounded-xl text-center hover:bg-slate-800 transition">
      <input
        type="file"
        accept="image/*"
        hidden
        onChange={(e) => onUpload(e.target.files[0])}
      />
      <p className="text-indigo-300">
        Click to upload image
      </p>
    </label>
  );
}
