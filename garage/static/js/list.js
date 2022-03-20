function escape(unsafe) {
    return unsafe
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

window.onload = () => {
    fetch("/api/v1/items").then(d => d.json()).then(items => {
        let table = $("#table");
        for (let item of items) {
            table.append(`<tr>
            <td>${escape(item.name)}</td>
            <td>${escape(item.kind)}</td>
            <td>${escape(item.note)}</td>
            <td>${item.price}ドル</td>
            <td><img src="${escape(item.photo_data)}" /></td>
            </tr>`);
        }
    });
}