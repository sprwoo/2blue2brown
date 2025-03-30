import { useEffect, useState } from "react";

export default function Dashboard() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    const fetchData = async () => {
      const token = localStorage.getItem("access_token");
      const res = await fetch("http://localhost:5001/api/protected", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      const json = await res.json();
      setData(json);
    };

    fetchData();
  }, []);

  return <pre>{JSON.stringify(data, null, 2)}</pre>;
}
