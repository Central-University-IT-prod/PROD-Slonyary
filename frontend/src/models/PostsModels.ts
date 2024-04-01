export type TPostItem = {
  channelAvatar: string,
  channelName: string,
  date: string,
  publicised: boolean,
  admin: string,
  postImages: string[],
  category: 'pending' | 'moderation' | 'published',
  ownerName: string,
  htmlText?: string,
  plainText?: string
}
