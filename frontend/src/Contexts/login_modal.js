import React from "react"

export const login_modal = {
    show: {
      show_login_modal:true
    },
    hide: {
        show_login_modal:false
    },
  };
  
  export const LoginContext = React.createContext(
    login_modal.hide // default value
  );