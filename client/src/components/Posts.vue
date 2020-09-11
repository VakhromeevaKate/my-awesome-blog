<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Posts</h1>
        <hr><br><br>
        <button type="button" v-b-modal.post-modal class="btn btn-success btn-sm">Add Post</button>
        <br><br>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col">Title</th>
            <th scope="col">Author</th>
            <th scope="col">Date</th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(post, index) in posts" :key="index">
            <td>{{ post.title }}</td>
            <td>{{ post.author }}</td>
            <td>{{ post.date }}</td>
            <td>
              <button type="button" class="btn btn-warning btn-sm">Update</button>
              <button type="button" class="btn btn-danger btn-sm">Delete</button>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addPostModal"
             id="post-modal"
             title="Add a new book"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-title-group"
                      label="Title:"
                      label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addPostForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Author:"
                      label-for="form-author-input">
          <b-form-input id="form-author-input"
                        type="text"
                        v-model="addPostForm.author"
                        required
                        placeholder="Enter author">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-text-group"
                      label="Text:"
                      label-for="form-text-input">
          <b-form-input id="form-text-input"
                        type="text"
                        v-model="addPostForm.text"
                        required
                        placeholder="Enter text">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      posts: [],
      addPostForm: {
        title: '',
        author: '',
        text: ''
      },
    };
  },
  methods: {
    getPosts() {
      const path = 'http://localhost:5000/posts';
      axios.get(path)
        .then((res) => {
          this.posts = res.data.posts;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addPost(payload) {
      const path = 'http://localhost:5000/posts';
      axios.post(path, payload)
        .then(() => {
          this.getPosts();
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.log(error);
          this.getPosts();
        });
    },
    initForm() {
      this.addPostForm.title = '';
      this.addPostForm.author = '';
      this.addPostForm.text = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addPostModal.hide();
      const payload = {
        title: this.addPostForm.title,
        author: this.addPostForm.author,
        text: this.addPostForm.text
      };
      this.addPost(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addPostModal.hide();
      this.initForm();
    },
  },
    created() {
      this.getPosts();
    },
  }
</script>
