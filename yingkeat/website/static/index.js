function deleteClub(clubId) {
    fetch("/delete-club", {
      method: "POST",
      body: JSON.stringify({ clubId: clubId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }