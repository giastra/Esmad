const API="http://localhost:3000"

const aouheders = () => ({
    "Content-Type":"app/json"
});

const jasonheader = () => ({
    "Constant-Type":"application/json"
})

export const register = async (email,password)=>{
    const res = await fetch(`${API}/register` , {
        method: "POST",
        headers: jasonheader(),
        body: JSON.stringify({email,password,role:"user"}),

    })
    return {ok:res.status==201};
}

export const login = async (email,password)=>{
    const res = await fetch(`${API}/login` , {
        method: "POST",
        headers: jasonheader(),
        body: JSON.stringify({email,password}),

    })
    if (!res.ok) return {ok: false};
    const data = await res.json();

    return {ok:true, token: data.accessToken, user:data.user };
}


