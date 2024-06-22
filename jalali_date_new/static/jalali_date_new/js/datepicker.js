window.onload = function () {
    jalaliDatepicker.startWatch(
        {
            separatorChars: {
                date: "-"
            },
            time: true,
            zIndex: 999999999,
            hasSecond: false,
            hideAfterChange: true,
        }
    );
}
