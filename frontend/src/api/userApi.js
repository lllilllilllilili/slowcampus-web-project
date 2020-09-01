import Axios from "axios";
// import store from "../vuex/store.js";
const URL = "http://localhost:8080"
const requestLogin = (data, callback, errorCallback) =>{
    
    
    const params = new URLSearchParams();
    console.log(data.user_id);
    console.log(data.user_pw);
    params.append('user_id', data.user_id);
    params.append('user_pw', data.user_pw);
    Axios.post(URL + '/api/user/signup', params)
    .then(response =>{
        callback(response.data);
        console.log("response : " +response);
        
        // store.commit('login', payload)
    }).catch(exp => {
        errorCallback(exp);
    })

}


const userApi={
     requestLogin: (data, callback, errorCallback) => requestLogin(data, callback, errorCallback),

}
export default userApi;