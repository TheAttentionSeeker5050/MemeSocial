const login_api = async (username, password, success, fail) => {
    // we will use this api call to authenticate login
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
    // handle the http response
    if (response.status === 200) {
      console.log("success", JSON.parse(text));
      success(JSON.parse(text));
    } else {
      console.log("failed", text);
      Object.entries(JSON.parse(text)).forEach(([key, value])=>{
        fail(`${key}: ${value}`);
      });
    }
  };