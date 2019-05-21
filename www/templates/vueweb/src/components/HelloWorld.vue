<template>
  <div class="hello">
      <div id="page">
    <div class="header">
      <span>文字识别</span>
    </div>
    <div class="main">
      <el-card>
        <span class="loginSpan">登录</span>
        <el-form :model="pcLoginData" :rules="rules" >
          <el-form-item prop="username" label="用户名">
            <el-input class="loginInput"  placeholder="请输入用户名" clearable></el-input>
          </el-form-item>
          <el-form-item prop="password" label="密码">
            <el-input class="loginInput" type="password" placeholder="请输入密码" clearable></el-input>
          </el-form-item>
          <el-button class="buttomButt" type="primary" @click="login()">登录</el-button>
        </el-form>
      </el-card>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data(){
    return{}
    },
  methods:{
    login(){
      var _this=this;
      console.log(this);
      this.$axios({
      method:'post',
      url:'/',
      data:{
        account:this.pcLoginData.username,
        password:this.pcLoginData.password,
        }
        }).then(function (response) {
          alert("登录成功！");
          _this.$router.push("/upload");
          })
          .catch(error=>{console.log(error);});
          }
          }
}
</script>
<style scoped>
  .header{
    padding-left: 50px;
    height: 80px;
    line-height: 80px;
    font-size: 30px;
    color: #409EFF;
    text-align: left;
  }
  .el-card{
    margin: 60px auto;
    height: 320px;
    width: 500px;
    padding: 20px 20px;

  }
  .loginSpan{
    height: 40px;
    font-size: 20px;
    color: #606266;
  }
  .el-form{
    margin-top: 10px;
  }
  .el-form-item{
    magin:5px 0;
  }
  .buttomButt{
    height: 40px;
    width: 80%;
    font-size: 20px;
    margin-top: 25px;
  }
  .el-radio__label{
    font-size: 20px;
  }
</style>
