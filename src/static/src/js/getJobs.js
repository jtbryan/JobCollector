import React, { useEffect } from 'react';
import axios from 'axios';

function GetJobs() {
  const [data, setData] = React.useState([])

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/get-jobs/')
      .then(response => {
        setData(response.data);
        console.log(response)
      })
      .catch(error => {
        console.log(error);
      });
  }, []);


  return (
    <div>
      {(() => {
        let arr = []

        for (let i = 0; i < 4; i++) {
          arr.push(<p>{data[i].id}</p>)
        }

        return arr
      })()};
    </div>
  );
}

export default GetJobs;