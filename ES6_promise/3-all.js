import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then(([photoResponse, userResponse]) => {
      console.log(photoResponse.body);
      console.log(userResponse.firstName, userResponse.lastName);
    })
    .catch(() => {
      console.log("Signup system offline");
    });
}

export default handleProfileSignup;
