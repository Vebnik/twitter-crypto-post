# libs
import os

class Config:

  @staticmethod
  def get_create_tweet_payload(tweet_text: str) -> dict:
    return {
      "variables": {
        "tweet_text": tweet_text,
        "dark_request": False,
        "media": {
          "media_entities": [],
          "possibly_sensitive": False
        },
        "withDownvotePerspective": False,
        "withReactionsMetadata": False,
        "withReactionsPerspective": False,
        "withSuperFollowsTweetFields": True,
        "withSuperFollowsUserFields": True,
        "semantic_annotation_ids": [],
        "conversation_control": {
            "mode": "ByInvitation"
        }
      },
      "features": {
        "view_counts_public_visibility_enabled": True,
        "view_counts_everywhere_api_enabled": True,
        "tweetypie_unmention_optimization_enabled": True,
        "responsive_web_uc_gql_enabled": True,
        "vibe_api_enabled": True,
        "responsive_web_edit_tweet_api_enabled": True,
        "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
        "interactive_text_enabled": True,
        "responsive_web_text_conversations_enabled": False,
        "responsive_web_twitter_blue_verified_badge_is_enabled": True,
        "verified_phone_label_enabled": False,
        "standardized_nudges_misinfo": True,
        "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
        "responsive_web_graphql_timeline_navigation_enabled": True,
        "responsive_web_enhance_cards_enabled": True
      },
      "queryId": os.getenv('TW_QUERI_ID')
    }