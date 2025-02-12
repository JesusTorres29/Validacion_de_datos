import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import axios from "axios";

const UserDataTable = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  // Función para obtener datos desde la API
  const fetchData = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/users/api/");
      setData(response.data);
      setLoading(false);
    } catch (error) {
      console.error("Error al cargar los datos:", error);
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData(); 
  }, []);

const handleEdit = async (user) => {
    const token = localStorage.getItem("accessToken");
    console.log("Token enviado:", token); 

    if (!token) {
      alert("No estás autenticado");
      return;
    }

    const newName = prompt("Nuevo nombre para " + user.name, user.name);
    if (newName) {
      try {
        const response = await axios.put(
          `http://127.0.0.1:8000/users/api/${user.id}/`,
          { ...user, name: newName },
          { headers: { Authorization: `Bearer ${token}` } }
        );
        console.log("Respuesta del servidor:", response.data); 
        fetchData(); 
      } catch (error) {
        console.error("Error al editar usuario:", error.response || error);
      }
    }
};


 const handleDelete = async (id) => {
  const token = localStorage.getItem("accessToken");
  if (!token) {
    alert("No estás autenticado");
    return;
  }

  if (window.confirm("¿Seguro que quieres eliminar este usuario?")) {
    try {
      await axios.delete(`http://127.0.0.1:8000/users/api/${id}/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      fetchData();
    } catch (error) {
      if (error.response) {
        alert(error.response.data.detail); 
      } else {
        console.error("Error al eliminar usuario:", error);
      }
    }
  }
};
  const columns = [
    { name: "Nombre", selector: (row) => row.name, sortable: true },
    { name: "Email", selector: (row) => row.email, sortable: true },
    { name: "Teléfono", selector: (row) => row.tel },
    {
      name: "Acciones",
      cell: (row) => (
        <span>
          <button className="btn btn-warning me-2" onClick={() => handleEdit(row)}>
            <i className="bi bi-pencil"></i>
          </button>
          <button className="btn btn-danger" onClick={() => handleDelete(row.id)}>
            <i className="bi bi-trash"></i>
          </button>
        </span>
      ),
    },
  ];

  return (
    <div>
      <h3>Tabla de usuarios</h3>
      <DataTable
        columns={columns}
        data={data}
        progressPending={loading}
        pagination
        highlightOnHover
        pointerOnHover
      />
    </div>
  );
};

export default UserDataTable;
