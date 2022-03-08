const login_api = async (username, password, success, fail) => {
    console.log("user api request")
    const response = await fetch(
          `http://127.0.0.1:8000/api/token/`,
          {
              method: 'POST',
              headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                "username": username,
                "password": password,
              })
          }
      );
    const text = await response.text();
    if (response.status === 200) {
      console.log("success", JSON.parse(text));
      console.log(JSON.parse(text))
      success(JSON.parse(text));
    } else {
      console.log("failed", text);
      Object.entries(JSON.parse(text)).forEach(([key, value])=>{
        fail(`${key}: ${value}`);
    });
    console.log(text)
    }
  };


export {login_api}