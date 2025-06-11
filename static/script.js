document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("registerForm");
  const resultDiv = document.getElementById("result");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = {
      email: document.getElementById("email").value,
      name: document.getElementById("name").value,
      phone: document.getElementById("phone").value,
      year: document.getElementById("year").value,
      semester: document.getElementById("semester").value,
      mode: document.getElementById("mode").value,
      type: document.getElementById("type").value,
    };

    fetch("/submit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
    .then((res) => res.json())
    .then((data) => {
      resultDiv.innerHTML = `<h3>✅ ${data.message}</h3>
        <p><strong>Email:</strong> ${formData.email}</p>
        <p><strong>Name:</strong> ${formData.name}</p>
        <p><strong>Phone:</strong> +91 ${formData.phone}</p>
        <p><strong>Year:</strong> ${formData.year}</p>
        <p><strong>Semester:</strong> ${formData.semester}</p>
        <p><strong>Mode:</strong> ${formData.mode}</p>
        <p><strong>Type:</strong> ${formData.type}</p>
      `;
      resultDiv.classList.remove("hidden");
      form.reset();
    })
    .catch((err) => {
      resultDiv.innerHTML = `<p style="color:red;">❌ Error submitting form.</p>`;
      resultDiv.classList.remove("hidden");
    });
  });
});
