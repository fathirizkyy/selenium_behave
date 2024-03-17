Feature: Fitur Login
   
   @login @loginsukses
   Scenario: Melakukan Login Sukses
      Given Masuk ke login page
      When memasukan username dan password valid berupa "standard_user" dan "secret_sauce"
      And menekan tombol login
      Then masuk dan menampilkan produk yang dijual
    
   @login @logingagalusername
   Scenario: Melakukan Login Gagal Invalid Username
      Given Masuk ke login page
      When memasukan username invalid berupa "username"
      And menekan tombol login
      Then menampilkan alert bahwa username and password not match
    
   @login @logingagalpassword
   Scenario: Melakukan Login Gagal Invalid Password
      Given Masuk ke login page
      When memasukan password invalid berupa "password"
      And menekan tombol login
      Then menampilkan alert bahwa username and password not match
    
   @login @logingagalusernamekosong
   Scenario: Melakukan Login Gagal Username Kosong
      Given Masuk ke login page
      When tidak memasukan username
      And menekan tombol login
      Then menampilkan alert bahwa Username is required
    
   @login @logingagalpasswordkosong
   Scenario: Melakukan Login Gagal Password Kosong
      Given Masuk ke login page
      When tidak memasukan password
      And menekan tombol login
      Then menampilkan alert bahwa password is required