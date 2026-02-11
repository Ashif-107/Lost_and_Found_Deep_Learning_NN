import { useState } from "react";
import api from "../services/api";
import ImageUpload from "../components/ImageUpload";

export default function AddItem() {
    const [image, setImage] = useState(null);
    const [imagePreview, setImagePreview] = useState(null);
    const [desc, setDesc] = useState("");

    const handleImageUpload = (file) => {
        setImage(file);
        // Create preview
        if (file) {
            const reader = new FileReader();
            reader.onloadend = () => {
                setImagePreview(reader.result);
            };
            reader.readAsDataURL(file);
        }
    };

    const handleUpload = async () => {
        if (!image || !desc) {
            alert("Please select image and description");
            return;
        }

        try {
            const formData = new FormData();
            formData.append("image", image);        // MUST be "image"
            formData.append("description", desc);   // MUST be "description"

            const res = await api.post("/upload", formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });

            console.log(res.data);
            alert("Item uploaded successfully!");
        } catch (err) {
            console.error(err.response?.data || err);
            alert("Upload failed");
        }
    };


    return (
        <div className="max-w-xl mx-auto mt-16 space-y-6">
            <h2 className="text-3xl font-bold">Add Found Item ➕</h2>
            <div className="flex flex-col items-center space-y-4">
                <ImageUpload onUpload={handleImageUpload} />
                {imagePreview && (
                    <div className="mt-4 w-full">
                        <img
                            src={imagePreview}
                            alt="Preview"
                            className="w-full h-64 object-cover rounded-lg"
                        />
                    </div>
                )}
                <input
                    className="w-full p-3 rounded bg-slate-800"
                    placeholder="Description"
                    onChange={(e) => setDesc(e.target.value)}
                />
                <button
                    onClick={handleUpload}
                    className="bg-indigo-500 px-6 py-3 rounded-lg hover:bg-indigo-600"
                >
                    Upload
                </button>

            </div>
        </div>
    );
}
