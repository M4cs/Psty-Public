<div align="center">
  <a href="https://psty.io"><img src="https://psty.io/assets/images/thumb.png" width="75%"></a>
  <h1>:pencil: psty.io :pencil:</h1>
</div>

### :star: What is psty.io? :star:

psty is a free, open source project that provides a service for sharing and highlighting source code/plaintext. It is written in Python with the Flask framework and available for integration to your own platform. You would be able to host this anywhere. This source code is setup to run on https://psty.io but you can run it on any site by changing the domains in the files.

### :star: How does it work? :star:

psty runs on Flask which can run on a number of platforms. I use UWSGI and Nginx to run my API through the domain but you can use other setups as well. It takes advantage of the [prism.js](https://prismjs.com) library which will allow you to render syntax highlighted source code from a plaintext string. You can check the source code for specifics on how it works logically.

### :star: Why would I want this? :star:

If you want to have a paste-service linked to your website that is pretty much fully customizable you can use this. This is a very easy way to share source code quickly and easily.
