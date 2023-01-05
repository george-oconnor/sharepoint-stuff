from src.sharepoint_stuff import getCTX, uploadFile

ctx = getCTX("https://ioedub.sharepoint.com/sites/AttendanceTest/", "goconnor@instituteofeducation.ie", "Welcome2IOE!")

uploadFile(ctx, "test.docx", "test.docx", "Shared Documents")