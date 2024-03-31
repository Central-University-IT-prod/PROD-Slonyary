import React, { useMemo, useState } from 'react';
import './ImageMessageContent.css'
import '../../styles/photoView.css';
import { MediaProvider } from '../../components/MediaProvider/MediaProvider';
import MediaView from '../MediaView/MediaView';
import { maxVisibleMedia } from '../../constans';
import { REACT_STATIC_URL } from '../../API/constans';

const ImageMessageContent = ({ messageData }) => {
    const { media } = messageData
    const [sortedMedia, setSortedMedia] = useState(media.sort((a, b) => Number(a.indexInMes) - Number(b.indexInMes)));
    const len = sortedMedia?.length;
    const mediaUrls = sortedMedia?.map(i => i.url)
    const [isViewMedia, setIsViewMedia] = useState(len > maxVisibleMedia ? 'hidden' : '');

    const getImagesForClient = (startIndex, lenght) => {
        const result = []

        for (let i = startIndex; i < lenght; i += 2) {
            const url = mediaUrls[i]
            const type = sortedMedia[i].type

            if (!url) return;
            const src = `${REACT_STATIC_URL}/${url}`

            switch (type) {
                case 'image':
                    result.push((
                        <MediaView index={i} key={i} src={src} mediaType='image'>
                            <img className='image-item' src={src} loading='lazy' />
                        </MediaView>
                    ))
                    continue;
            }

        }

        return result
    };

    const fistColum = useMemo(() => getImagesForClient(0, len), [sortedMedia])
    const secondColum = useMemo(() => getImagesForClient(1, len), [sortedMedia])

    const classGenerate = (commonClass) => `${commonClass} ${isViewMedia}`;

    const seeAllMedia = () => setIsViewMedia('')

    return len > 0 && (
        <div className='ImageMessageContent'>
            <div className='image-table'>
                <MediaProvider mediaCount={len}>
                    <div className={classGenerate('colum-1')}>
                        {fistColum}
                    </div>
                    {len > 1 &&
                        <div className={classGenerate('colum-2')}>
                            {secondColum}
                        </div>
                    }
                </MediaProvider>
            </div>
            {isViewMedia === 'hidden' && (
                <button className="seeAllBtn" onClick={seeAllMedia}>
                    <p>Смотреть все медиа</p>
                </button>
            )}
        </div>
    );
}

export default ImageMessageContent;
