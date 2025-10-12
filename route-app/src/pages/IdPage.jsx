import { useParams, useNavigate } from "react-router-dom";
import { useEffect } from "react";

export default function IdPage() {
  const { id } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    if (parseInt(id) > 100) {
      navigate("/");
    }
  }, [id, navigate]);

  return (
    <div>
      <h2>ID da Página: {id}</h2>
    </div>
  );
}
