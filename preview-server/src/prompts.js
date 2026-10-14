// Server-side prompt catalogue. The storefront only sends a category + style
// name; anything not listed here is rejected, so customers can never send
// their own prompt text to the image model.

const PORTRAIT_SIZE = '1024x1536'; // 2:3 — matches 12×18, 16×24 and 24×36 prints
const ROUND_SIZE = '1024x1024';

const IDENTITY = [
  'Use the uploaded photo as the reference for every person and animal in it.',
  'Keep each subject instantly recognisable: same face shape, facial features, skin tone, age, hair, eye colour, glasses, and the colours of their clothing.',
  'Do not beautify, slim, de-age or change anyone. Keep the same number of people and animals.',
].join(' ');

const JESUS = 'Jesus is depicted as a gentle, kind man with shoulder-length brown hair, a short beard and a soft cream-and-tan robe, with a calm, loving expression.';

const PAINTERLY = 'Rendered as a warm devotional fine-art painting: soft watercolor and oil textures, golden-hour light, cream and honey tones, delicate paint splashes fading to a light background at the edges.';

const SAFE = 'Tasteful, peaceful and respectful. No text, no lettering, no logos, no watermarks, no frames. Portrait orientation.';

const STAINED_GLASS = 'Rendered as a round leaded stained-glass suncatcher disc: the background, robes and clothing are made of jewel-toned glass panes joined by dark lead lines, while the faces and hands stay softly painted and true to the photo. Light glowing through the glass. The circular disc fills the whole square image on a plain white background. No text, no logos.';

function portrait(scene) {
  return { prompt: `${IDENTITY} ${scene} ${JESUS} ${PAINTERLY} ${SAFE}`, size: PORTRAIT_SIZE };
}

function glass(scene) {
  return { prompt: `${IDENTITY} ${scene} ${JESUS} ${STAINED_GLASS}`, size: ROUND_SIZE };
}

export const STYLES = {
  classic: {
    'warm': portrait('Jesus stands just behind the subjects with His arms gently around their shoulders in a warm embrace, all of them close together and smiling.'),
    'walking': portrait('Jesus walks side by side with the subjects along a sunlit country path by a river at golden hour, His hand resting on a shoulder.'),
    'preaching': portrait('The subjects sit beside Jesus on a grassy hillside as He reads to them from an open book, a quiet teaching moment in soft afternoon light.'),
    'memorial': portrait('A heavenly memorial tribute: the subjects rest peacefully in Jesus\' embrace among soft clouds and warm light, with gentle feathered angel wings behind them.'),
  },
  pets: {
    'held-by-jesus': portrait('Jesus cradles the pet (dog or cat) lovingly in His arms, cheek close to the animal. If people are in the photo, they stand beside Him.'),
    'walking-together': portrait('Jesus walks along a sunny meadow path with the pet trotting happily at His side.'),
    'rainbow-bridge': portrait('A memorial scene: the pet sits beside Jesus at the foot of a soft pastel rainbow bridge over a gentle stream, peaceful and content.'),
    'heavenly-rest': portrait('A memorial scene: the pet rests peacefully curled up beside a seated Jesus on soft clouds, with a faint golden halo of light around the animal.'),
  },
  riders: {
    'riding-together': portrait('The rider sits on their own vehicle exactly as it appears in the photo (motorcycle, truck or car — keep its make, colour and details), with Jesus standing beside them, a hand on their shoulder, on an open road at sunset.'),
    'open-highway': portrait('A wide open highway through golden plains at sunset; the rider and their vehicle from the photo travel the road while Jesus watches over them from the roadside.'),
    'road-guardian': portrait('Jesus stands protectively behind the rider and their vehicle from the photo, one hand raised in blessing, soft light around them on a quiet road.'),
    'last-ride-memorial': portrait('A memorial tribute: the rider and their vehicle from the photo ride toward a glowing sunset horizon on a heavenly road among soft clouds, with Jesus walking beside them.'),
  },
  kids: {
    'held-in-his-arms': portrait('Jesus holds the child gently and protectively in His arms, the child safe, calm and comforted. Omit any hospital equipment, tubes or bandages, and keep the child\'s own hair or lack of hair exactly as in the photo.'),
    'brave-little-warrior': portrait('The child stands proudly beside Jesus, who kneels to their level with a hand on their shoulder, both smiling — a picture of courage and comfort. Omit any hospital equipment, tubes or bandages, and keep the child\'s own hair or lack of hair exactly as in the photo.'),
    'little-angel': portrait('A memorial tribute: the child, with small soft feathered angel wings, sits peacefully on Jesus\' lap among soft clouds and warm light.'),
    'playing-in-heaven': portrait('A memorial tribute: the child plays happily in a sunlit heavenly meadow of flowers while Jesus sits nearby watching with a gentle smile.'),
  },
  grandparents: {
    'mom-dad-together': portrait('The couple stands close together with Jesus behind them, His arms around both of their shoulders. If the photo shows only one of them, keep only that person.'),
    'mom-with-jesus': portrait('The mother (the woman in the photo) is embraced warmly by Jesus, her head resting near His shoulder.'),
    'dad-with-jesus': portrait('The father (the man in the photo) stands beside Jesus, who has a hand on his shoulder; both smile warmly.'),
    'memorial-tribute': portrait('A heavenly memorial tribute: the subjects rest peacefully in Jesus\' embrace among soft clouds and warm light.'),
  },
  wedding: {
    'sacred-vows': portrait('The couple, in the wedding clothes from the photo, holds hands while Jesus stands behind them blessing their union with His hands resting on their shoulders.'),
    'golden-hour': portrait('The couple from the photo embraces in a golden-hour field with Jesus standing nearby smiling in blessing.'),
    'first-dance': portrait('The couple from the photo shares their first dance in soft warm light while Jesus watches lovingly from beside them.'),
    'anniversary': portrait('The couple from the photo sits together on a garden bench with Jesus seated beside them, a celebration of a lifetime of love.'),
  },
  suncatcher: {
    'warm': glass('Jesus embraces the subjects from behind with His arms around their shoulders.'),
    'walking': glass('Jesus walks beside the subjects on a sunlit path.'),
    'memorial': glass('A memorial: the subjects rest in Jesus\' embrace with soft angel wings behind them.'),
  },
  'pet-suncatcher': {
    'warm': glass('Jesus cradles the pet lovingly in His arms.'),
    'halo': glass('The pet sits beside Jesus with a gentle golden halo above its head.'),
    'memorial': glass('A memorial: the pet rests beside Jesus with small angel wings and a halo.'),
  },
};

export function slug(s) {
  return String(s || '')
    .toLowerCase()
    .replace(/&/g, ' ')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

/** Returns { prompt, size } or null when the category/style is unknown. */
export function lookupStyle(category, styleName) {
  const cat = STYLES[slug(category)] ? slug(category) : 'classic';
  return STYLES[cat][slug(styleName)] || null;
}
