<template>
  <el-container>
    <el-header>
      <div class="header">
      <div class="top"></div>
      <div class='top-text'>图像文字识别系统</div>
      <el-button type='text' class="exit" @click="loginOut">退出系统</el-button>
    </div>
      
    </el-header>
  
    <el-main>
      <div class=back>
          <!-- <img class='sky' src='./assets/back2.jpg' /> -->
          <img class='cloud' src='https://tinypng.com/images/jpg/cloud-left.png' />
          <img class='cloud2' src='https://tinypng.com/images/jpg/cloud-left.png' />
          <div v-if="!resultShow">
            <img class='bamboo' src='https://tinypng.com/images/bamboo.png' />
            <img class='panda' src='https://tinypng.com/images/panda-chewing.png' />
            <img class='grass' src='https://tinypng.com/images/grass-confetti.png' />
            <div class='upload'>
            <el-upload
                  class="upload-demo"
                  ref="upload"
                  drag
                  :action="imgUrl"
                  :on-success="handleAvatarSuccess"
                  :on-change="handleChange"
                  :on-remove="handleRemove"
                  :file-list="fileList"
                  :limit="1"
                  :on-exceed="handleExceed"
                  :auto-upload="false">
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
              <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
            </el-upload>
          </div>
          </div>
          <div v-else>
            <img class='bamboo2' src='https://tinypng.com/images/bamboo.png' />
            <img class='panda2' src='https://tinypng.com/images/panda-happy.png' />
            <img class='grass2' src='https://tinypng.com/images/grass-confetti.png' />
          </div>
          
      </div>
      <div v-if="!resultShow" class="biaoti">
        <el-button type="success" @click='refersh()'>重置</el-button>
        <el-button type="primary" @click='submitUpload()'>解析</el-button>
      </div>
      <div v-else>
        <div class="result">
          <el-input class="result-block" id="result" type="textarea" :autosize="{ minRows: 7, maxRows: 12}" v-model="result">
          </el-input>
        </div>
        <div class="result-button">
          <el-button type="primary" @click='goback'>再识别一张</el-button>
          <el-button type="success" @click='copy'>复制到剪贴板</el-button>
          </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
    export default {
        data() {
            return {
                imgUrl:"http://127.0.0.1:5000/upload/",
                fileList: [],
                file:[],
                resultShow:false,
                result:""
            }
        },
        created(){

        },

        methods: {
          loginOut(){
            this.$router.push({path:'/'})
          },
          goback(){
              this.resultShow=!this.resultShow;
          },
         handleAvatarSuccess(res, file) {
            this.iUrl = URL.createObjectURL(file.raw);
            console.log(this.iUrl);
             },
          handleChange(file,files){
            var that=this;
            this.file=file;
            this.length=files.length;
            this.response=file.response;
            if(this.response){
              console.log(this.response);
              if(this.response.status=="200"){
                alert("解析成功");
                that.result=this.response.text;
                that.dialogVisible=false;
              }else{
                alert("解析失败，请检查文件格式并重新上传");
                that.dialogVisible=false;
              } 
              }
            },
            handleRemove(file, fileList) {
              this.length=0;
              this.response=[];
            },
            handleExceed(files, fileList) {this.$message.warning(`当前文件列表中已有文件，请重置后再上传`);},
            submitUpload() {
              console.log(this.length);
              if(this.length>0){
              this.$refs.upload.submit();
              var that=this;
              let formData = new FormData();
              formData.append("file", this.file);
              this.resultShow=!this.resultShow;
              }
              else{
                alert("您还未选择文件");
              }
              
            },
            refresh() {
                this.$refs.upload.clearFiles();
            },
            copy(){
              var Url2=document.getElementById("result").innerText;
              var oInput = document.createElement('input');
              oInput.value = Url2;
              document.body.appendChild(oInput);
              oInput.select(); // 选择对象
              document.execCommand("Copy"); // 执行浏览器复制命令
              oInput.className = 'oInput';
              oInput.style.display='none';
              alert('复制成功');
            }
        },
         refresh() {
           this.$refs.upload.clearFiles();
           this.response=[];
            },
        mounted(){
          document.querySelector('body').setAttribute('style', 'background-color:#e7f0f3')
        },
        beforeDestroy() {
          document.querySelector('body').removeAttribute('style')
        } 
    }
</script>
<style scoped>
      body{
        background: #b9cdd4;
      }
      .top{
        width: 100%;
        height: 4rem;
        background: gray;
        position: fixed;
        top: 0;
        left:0;
        z-index:999;
      }
      .top-text{
        font-size: 1.3rem;
        color:burlywood;
        z-index:9999;
        position: fixed;
        top: 1rem;
        left: 5%;
      }
      .exit{
        font-size: 1.1rem;
        color:burlywood;
        z-index:9999;
        position: fixed;
        top: 0.7rem;
        right: 5%;
      }
      .back{
        width:100%;
        height: 100%;
        margin: 0 auto;
        margin-top: 50px;
        left:0;
        bottom:10rem;
        overflow: hidden;
      }
      .sky{
        position: absolute;
        z-index: 0;
        width: 100%;
        height: 35rem;
        bottom:0rem;
        left:0;
      }
      .cloud{
        position: absolute;
        z-index: 1;
        top: -2.4rem;
        left: -10%;
        width: 55.7rem;
        height: 22.3rem;
        -webkit-background-size: 55.7rem 22.3rem;
        -moz-background-size: 55.7rem 22.3rem;
        background-size: 55.7rem 22.3rem;
        background-repeat: no-repeat;
      }
      .cloud2{
        position: absolute;
        z-index: 1;
        top: -2.4rem;
        left: 20%;
        width: 55.7rem;
        height: 22.3rem;
        -webkit-background-size: 55.7rem 22.3rem;
        -moz-background-size: 55.7rem 22.3rem;
        background-size: 55.7rem 22.3rem;
        background-repeat: no-repeat;
      }
      .bamboo{
        position: absolute;
        z-index: 7;
        width: 25rem;
        height: 50rem;
        bottom:13rem;
        left: 67%;
      }
      .bamboo2{
        position: absolute;
        z-index: 7;
        width: 25rem;
        height: 50rem;
        bottom:0rem;
        left: 67%;
      }
      .panda{
        position: absolute;
        z-index: 7;
        width: 20rem;
        height: 18rem;
        bottom:13rem;
        left: 7%;
      }
      .panda2{
        position: absolute;
        z-index: 7;
        width: 22rem;
        height: 20rem;
        bottom:0rem;
        left: 7%;
      }
      .grass{
        position: absolute;
        z-index: 7;
        width: 100%;
        height: 2rem;
        bottom:13rem;
        left:0
      }
      .grass2{
        position: absolute;
        z-index: 7;
        width: 100%;
        height: 2rem;
        bottom:0rem;
        left:0
      }
      .upload{
        position: absolute;
        height:15rem;
        width: 100%;
        top:10rem;
        text-align: center;
        z-index:7;
      }
      .biaoti{
        position: absolute;
        width:100%;
        height:5rem;
        top:28rem;
        font-size: 1rem;
        text-align: center;
        line-height: 1.5rem;
        color:#40444F;
        font-family: "OpenSans",sans-serif;
      }
      .result{
        position: absolute;
        width:100%;
        height:5rem;
        top:10rem;
        font-size: 1rem;
        text-align: center;
        color:#40444F;
        font-family: "OpenSans",sans-serif;
        z-index:99;
      }
      .result-block{
        background: transparent;
        width:30rem;
        height: 30rem;
      }
      .result-button{
        position:absolute;
        width:100%;
        height:5rem;
        top:30rem;
        z-index:99;
        text-align: center;
      }
</style>

