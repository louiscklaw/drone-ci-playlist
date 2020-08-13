import React from 'react'

import api from '../api'

let default_value = {
  hello: "world"
}

const GlobalContext = React.createContext(default_value)

function GlobalContextProvider(props){
  let [hello, setHello] = React.useState(default_value.hello)

  React.useEffect(()=>{
    console.log('getting python_test_result')
    api.getAllPythonTestResult()
      .then( ( response ) => {
        // setResponseData(response.data)
        console.log( response )
        setPythonTestResult(response.data)
      } )
      .catch( ( error ) => {
        console.log( error )
        setPythonTestResult({error:"error during loading the result json"})
      } )
  },[])

  return(
    <GlobalContext.Provider value={{ hello, setHello }}>
      {props.children}
    </GlobalContext.Provider>
  )
}

export {GlobalContextProvider}
export default GlobalContext
