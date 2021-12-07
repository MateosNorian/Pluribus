import axios from "axios";
import Hand from "./components/Hand";
import React from "react";
import { v4 as uuidv4 } from "uuid";
import createCardObj from "./utils/createCardObj";

function App() {
  const [data, setData] = React.useState(null);

  React.useEffect(() => {
    axios.get("http://127.0.0.1:5000/api/hands").then((response) => {
      setData(response.data);
    });
  }, []);

  if (!data) return null;

  return (
    <>
      {data.map((arr) => {
        let hand = createCardObj(arr);
        return <Hand hand={hand} key={uuidv4()} />;
      })}
    </>
  );
}

export default App;
