const SHEET_NAME = '預測紀錄';
const HEADERS = [
  'code',
  'name',
  'sentAt',
  'event',
  'm1',
  'm2',
  'm3',
  'm4',
  'userAgent',
  'createdAt'
];

function doGet(e) {
  const params = e && e.parameter ? e.parameter : {};
  const callback = params.callback || 'callback';

  try {
    const action = params.action || 'list';
    if (action === 'submit') {
      const submission = JSON.parse(decodeURIComponent(params.payload || '{}'));
      validateSubmission_(submission);
      upsertSubmission_(submission);
      return jsonp_(callback, { ok: true, code: submission.code });
    }
    if (action === 'list') {
      return jsonp_(callback, { ok: true, items: listSubmissions_() });
    }
    return jsonp_(callback, { ok: false, error: 'unknown action' });
  } catch (error) {
    return jsonp_(callback, { ok: false, error: String(error && error.message ? error.message : error) });
  }
}

function validateSubmission_(submission) {
  if (!submission || typeof submission !== 'object') throw new Error('empty submission');
  if (!submission.code) throw new Error('missing code');
  if (!submission.name) throw new Error('missing name');
  if (!Array.isArray(submission.picks) || submission.picks.length !== 4) throw new Error('missing picks');
}

function upsertSubmission_(submission) {
  const sheet = getSheet_();
  const rows = sheet.getDataRange().getValues();
  const byCode = rows.findIndex((row, index) => index > 0 && row[0] === submission.code);
  const byName = rows.findIndex((row, index) => index > 0 && row[1] === submission.name);
  const pickMap = {};
  submission.picks.forEach((pick) => {
    pickMap[pick.id] = pick.pick;
  });
  const row = [
    submission.code,
    submission.name,
    submission.sentAt || '',
    submission.event || '',
    pickMap.m1 || '',
    pickMap.m2 || '',
    pickMap.m3 || '',
    pickMap.m4 || '',
    Session.getTemporaryActiveUserKey(),
    new Date()
  ];
  const targetIndex = byCode > 0 ? byCode : byName;
  if (targetIndex > 0) {
    sheet.getRange(targetIndex + 1, 1, 1, row.length).setValues([row]);
    return;
  }
  sheet.appendRow(row);
}

function listSubmissions_() {
  const sheet = getSheet_();
  const rows = sheet.getDataRange().getValues();
  if (rows.length <= 1) return [];
  return rows.slice(1).filter((row) => row[0] || row[1]).map((row) => ({
    code: row[0],
    name: row[1],
    sentAt: row[2],
    event: row[3],
    m1: row[4],
    m2: row[5],
    m3: row[6],
    m4: row[7]
  })).reverse();
}

function getSheet_() {
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = spreadsheet.getSheetByName(SHEET_NAME);
  if (!sheet) sheet = spreadsheet.insertSheet(SHEET_NAME);
  const firstRow = sheet.getRange(1, 1, 1, HEADERS.length).getValues()[0];
  const needsHeader = HEADERS.some((header, index) => firstRow[index] !== header);
  if (needsHeader) {
    sheet.getRange(1, 1, 1, HEADERS.length).setValues([HEADERS]);
    sheet.setFrozenRows(1);
  }
  return sheet;
}

function jsonp_(callback, payload) {
  const safeCallback = String(callback).replace(/[^\w$.]/g, '');
  return ContentService
    .createTextOutput(`${safeCallback}(${JSON.stringify(payload)});`)
    .setMimeType(ContentService.MimeType.JAVASCRIPT);
}
