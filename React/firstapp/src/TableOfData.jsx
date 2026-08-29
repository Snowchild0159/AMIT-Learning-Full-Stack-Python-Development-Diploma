import { useEffect, useState } from "react";
import { Link } from "react-router";
function TableOfData() {
  const [data, SetData] = useState([]);
  const [counter, SetCounter] = useState(0);
  const [loading, SetLoading] = useState(false);

  useEffect(() => {
    async function fetchData() {
      SetLoading(true);
      const response = await fetch("https://jsonplaceholder.typicode.com/posts");
      const records = await response.json();
      SetLoading(false);
      SetData(records.slice(0, 10));
    }
    fetchData();
  }, [counter]);

  function handleRefresh() {
    SetCounter(counter + 1);
  }

  return (
    <div>
      {loading ? (
        <p>Loading....</p>
      ) : data && data.length > 0 ? (
        <table class="table table-success table-striped">
          <thead>
            <tr>
              {Object.keys(data[0])?.map((ele) => (
                <th key={ele}>{ele?.toUpperCase()}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.map((person) => (
              <tr key={person.id}>
                {Object.keys(data[0])?.map((ele) => (
                  <td key={person.id + person[ele]}>
                    {person?.[ele] ??
                      `No ${ele?.[0]?.toUpperCase()}${ele?.slice(1)?.toLowerCase()}`}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No Data available</p>
      )}
      <button class="btn btn-primary" disabled={loading} onClick={handleRefresh}>
        refresh({counter})
      </button>
<li><Link to="/about">about</Link></li>
    </div>
    
  );
}
export default TableOfData;
