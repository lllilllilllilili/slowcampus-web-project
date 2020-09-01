import Axios from "axios";
// import store from "../vuex/store.js";
const URL = "http://localhost:3000"


const requestCategoryBasic = (data, callback, errorCallback) =>{
  
    Axios.post(URL + '/bigquery/?category='+data[0])
    .then(response=>{
      callback(response);
    }).catch(exp=>{
      console.log(exp);
      errorCallback(exp);
    })
}

const requestFeatureBasic = async(data, callback, errorCallback) =>{

  await Axios.post(URL + '/bigquery/feature/?category='+data)
  .then(response=>{
    callback(response);
  }).catch(exp=>{
    console.log(exp);
    errorCallback(exp);
  })
}

const requestCategoryAdvanced = async(data, callback, errorCallback)=>{
  console.log('requestCategoryAdvanced')
  console.log(data)
  await Axios.post(URL + '/bigquery/category_advanced/?category='+data)
  .then(response=>{
    callback(response);
  }).catch(exp=>{
    console.log(exp);
    errorCallback(exp);
  })
}
const requestCommit = async(data, callback, errorCallback)=>{
  await Axios.post(URL + '/bigquery/commit/?category='+data)
  .then(response=>{
    
    callback(response);
  }).catch(exp=>{
    console.log(exp);
    errorCallback(exp);
  })
}
const requestStreaming = async(data, callback, errorCallback)=>{
  console.log('requestStreaming!!!')
  await Axios.post(URL + '/bigquery/streaming/?category='+data)
  .then(response=>{
    callback(response);
  }).catch(exp=>{
    console.log(exp)
    errorCallback(exp)
  })
}

const proxyApi = {
  requestCategoryBasic: (data, callback, errorCallback) =>requestCategoryBasic(data, callback, errorCallback),
  requestFeatureBasic: (data, callback, errorCallback) => requestFeatureBasic(data, callback, errorCallback),
  requestCategoryAdvanced: (data, callback, errorCallback) => requestCategoryAdvanced(data, callback, errorCallback),
  requestCommit: (data, callback, errorCallback) =>requestCommit(data, callback, errorCallback),
  requestStreaming : (data, callback, errorCallback) => requestStreaming(data, callback, errorCallback),
}
export default proxyApi;