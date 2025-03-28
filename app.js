document.getElementById('image-upload-form').addEventListener('submit', async (event) => {
  event.preventDefault();

  const formData = new FormData();
  const imageFile = document.getElementById('image-file').files[0];
  formData.append('image', imageFile);

  try {
    const response = await fetch('/api/uploadImage', {
      method: 'POST',
      body: formData,
    });
    const data = await response.json();
    alert('Image uploaded successfully');
  } catch (error) {
    alert('Error uploading image');
  }
});
