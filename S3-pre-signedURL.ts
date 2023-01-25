import AWS, {S3} from "aws-sdk";

export const s3 = new S3({
    region: "리전",
    signatureVersion: "v4",
    accessKeyId: "엑세스 키 ID",
    secretAccessKey: "Secret 키",
});

// export async function getPresignedUrl(id: string, filename: string, ex: string) {
//     const params = {
//         Bucket: 's3 버킷',
//         Key: `객체명`,
//         // ContentType: 'image/*',
//         ContentType: 'multipart/form-data',
//         Expires: 10000,
//     };

//     const signedUrl = await s3.getSignedUrlPromise('putObject', params);

//     console.log(signedUrl);
//     return signedUrl;
// }
export async function getPresignedUrl(id: string) {
    const params = {
        Bucket: "s3 버킷",
        Key: `객체명`,
        // ContentType: 'image/*',
        ContentType: "application/json",
        Expires: 10000,
    };

    const signedUrl = await s3.getSignedUrlPromise("putObject", params);

    console.log(signedUrl);
    return signedUrl;
}
