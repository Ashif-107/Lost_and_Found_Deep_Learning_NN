import { useState } from "react";
import { useNavigate } from "react-router-dom";
import ImageUpload from "../components/ImageUpload";
import api from "../services/api";

export default function Home() {
    const [image, setImage] = useState(null);
    const [imagePreview, setImagePreview] = useState(null);
    const navigate = useNavigate();

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

    const handleSearch = async () => {
        try {
            const formData = new FormData();
            formData.append("image", image);

            const res = await api.post("/search", formData);
            console.log("Backend response:", res.data);

            navigate("/results", { state: res.data });
        } catch (err) {
            console.error("API error:", err);
            alert("Backend not reachable");
        }
    };

    return (
        <div className="max-w-xl mx-auto mt-20 text-center space-y-6">
            <h2 className="text-3xl font-bold">Find Your Lost Item 🔍</h2>
            <div className="flex flex-col items-center space-y-4">

                <ImageUpload onUpload={handleImageUpload} className="" />
                {imagePreview && (
                    <div className="mt-4 w-full">
                        <img
                            src={imagePreview}
                            alt="Preview"
                            className="w-full h-64 object-cover rounded-lg"
                        />
                    </div>
                )}
                <button
                    onClick={handleSearch}
                    disabled={!image}
                    className="bg-indigo-500 px-6 py-3 rounded-lg hover:bg-indigo-600 disabled:opacity-50"
                >
                    Search
                </button>
            </div>
        </div>
    );
}
