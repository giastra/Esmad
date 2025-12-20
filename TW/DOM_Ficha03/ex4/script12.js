let users = [
      {name: "Carlo", 
        username: "CarLow", 
        email:"carlo1234@gmail.com", 
        password: "carfast50"},
      
        {name: "Vikky", 
        username: "vikkySim", 
        email:"viksim2020@gmail.com", 
        password: "rosieBrown"},
      
        {name: "Ash", 
            username: "firestar", 
            email:"firestar456@gmail.com", 
            password: "teenTitans"}
    ]

    document.getElementById("butao").addEventListener("click", tudo)
    function tudo (e){
      e.preventDefault()
      let name = document.getElementById("name").value;
      let username = document.getElementById("username").value;
      let email = document.getElementById("email").value;
      let password = document.getElementById("password").value;

      // Verificar se existe utilizador
      let user = users.find(u => u.username === username);

      if(user){
        if(user.password === password){
          document.getElementById("mensagem").innerHTML = 
            `<p>Bem-vindo de volta, ${user.name}!</p>`;
        } else {
          document.getElementById("mensagem").innerHTML = 
            `<p style="color:red;">Password incorreta!</p>`;
        }
      } 
      
      else {
        // Registar novo utilizador
        users.push({name, username, email, password});
        document.getElementById("mensagem").innerHTML = 
          `<p>Bem-vindo, ${name}! Utilizador registado com sucesso.</p>`;
      }
    }
    